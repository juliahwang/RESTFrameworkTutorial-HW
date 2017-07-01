from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


# class SnippetSerializer(serializers.Serializer):
#     # 직렬화/반직렬화될 필드를 선언
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         max_length=100
#     )
#     # style={'base_template': 'textarea.html'} 는
#     # 장고 폼의 widget=widgets.Textarea 로 쓴 것과 같다.
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(
#         choices=LANGUAGE_CHOICES,
#         default='python',
#     )
#     style = serializers.ChoiceField(
#         choices=STYLE_CHOICES,
#         default='friendly'
#     )
#
#     def create(self, validated_data):
#         """
#         검증한 데이터로 새 'Snippet' 인스턴스를 생성하고 리턴
#         :param validated_data:
#         :return: 새 Snippet 인스턴스
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         검증한 데이터로 기존 'Snippet' 인스턴스를 업데이트한 후 리턴
#         :param instance: Snippet의 인스턴스
#         :param validated_data: 검증한 데이터
#         :return: 인스턴스 수정후 리턴
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# 모델 시리얼라이저 정의하기
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight',
        format='html',
    )

    class Meta:
        model = Snippet
        fields = (
            # 'id', - hyperlink로 관계정의. 필요없음.
            'title',
            'code',
            'linenos',
            'language',
            'style',
            # owner를 새로 정의해주었으므로 반드시 추가!
            'owner',
            # Hyperlink 방식의 시리얼라이저에 필드추가, url포함
            'url',
            'highlight',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all(),
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            # 'id',
            # id(pk) 대신 url 추가
            'url',
            'username',
            'snippets'
        )
