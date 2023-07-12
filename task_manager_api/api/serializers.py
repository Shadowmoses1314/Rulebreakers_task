from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=150,
        error_messages={
            'blank': 'Отсутствует название задачи',
            'required': 'Отсутствует поле названия задачи',
        }
    )

    description = serializers.CharField(
        error_messages={
            'blank': 'Отсутствует описание задачи',
            'required': 'Отсутствует поле описания задачи',
        }
    )

    completed = serializers.BooleanField(
        error_messages={
            'invalid': 'True или False',
        }
    )
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',
                                           read_only=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'created_at']
