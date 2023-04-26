from django.core.management.base import BaseCommand, CommandParser, CommandError
from users.models import User


class Command(BaseCommand):
    help = "Create users"

    def add_arguments(self, parser: CommandParser) -> None:

        parser.add_argument(
            "username", nargs="?", type=str, help="Define username."
        )

        parser.add_argument(
            "email", nargs="?", type=str, help="Define email."
        )
        parser.add_argument(
            "password", nargs="?", type=str, help="Define password."
        )

    def handle(self, *args: tuple, **options: dict) -> str | None:
        username_get = options.get("username") or "admin"
        email_get = options.get("email") or (f"{username_get}@example.com")
        password_get = options.get("password") or "admin1234"

        username_user = User.objects.filter(username=username_get)

        if username_user:
            raise CommandError(f"Username `{username_get}` already taken.")

        email_user = User.objects.filter(email=email_get)

        if email_user:
            raise CommandError(f"Email `{email_get}` already taken.")

        User.objects.create_superuser(username=username_get, password=password_get, email=email_get)

        self.stdout.write(self.style.SUCCESS(f"Admin `{username_get}` successfully created!"))
