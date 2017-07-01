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
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'owner',
        )


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all(),
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
