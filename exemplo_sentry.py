# Importando bibliotecas de terceiros
import sentry_sdk

sentry_sdk.init(
    dsn=(
        "https://60c1257f99a2d2c87f1eb1bc54d472bf@o4509016367628288"
        ".ingest.us.sentry.io/4509016374640640"
    ),
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/
    #  for more info
    send_default_pii=True,
)

division_by_zero = 1 / 0
