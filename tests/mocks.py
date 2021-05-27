from unittest.mock import Mock

User = Mock(
    query=Mock(
        all=Mock(
            return_value=[
                Mock(
                    id=7,
                    first_name='Guido',
                    last_name='van Rossum'
                )
            ]
        )
    )
)

mocked_function = Mock(return_value=['1', '3', '6'])

print(User.query.all()[0].id)
print(mocked_function())