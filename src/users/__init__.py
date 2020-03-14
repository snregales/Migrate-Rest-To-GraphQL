class UserConst:
    F_NAME: str = 'first_name'
    L_NAME: str = 'last_name'
    EMAIL: str = 'email'
    PASS: str = 'password'
    STAFF: str = 'is_staff'
    ACTIVE: str = 'is_active'
    SUPER: str = 'is_superuser'
    FULL: str = 'fullname'
    SHORT: str = 'short_name'


EMAIL_NOT_SET = f'The given {UserConst.EMAIL} must be set.'
