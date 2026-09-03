from app.infrastructure.mixins import IdMixin
from app.infrastructure.mixins import TimestampMixin


def main() -> None:
    print("IdMixin:", IdMixin)
    print("TimestampMixin:", TimestampMixin)


if __name__ == "__main__":
    main()