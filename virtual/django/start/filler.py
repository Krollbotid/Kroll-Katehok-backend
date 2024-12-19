from django.db import IntegrityError
from support.models import TicketStatus


def filler():
    statuses = [
        {"name": "Ожидание", "description": "Заявка ожидает обработки."},
        {"name": "Отвечено", "description": "На заявку был дан ответ."},
    ]

    for status_data in statuses:
        try:
            status, created = TicketStatus.objects.get_or_create(
                name=status_data["name"],
                defaults={"description": status_data["description"]},
            )
            if created:
                print(f"Статус '{status.name}' успешно создан.")
            else:
                print(f"Статус '{status.name}' уже существует.")
        except IntegrityError as e:
            print(f"Ошибка при создании статуса '{status_data['name']}': {e}")


if __name__ == "__main__":
    filler()
