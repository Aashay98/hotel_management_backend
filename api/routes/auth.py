from api.services.authentication import change_password, login, reset_password, signup


def configure(app):
    app.add_url_rule('/login',
                        view_func=login,
                        methods=['POST'])
    app.add_url_rule('/change_password',
                        view_func=change_password,
                        methods=['POST'])
    app.add_url_rule('/reset_password',
                        view_func=reset_password,
                        methods=['POST'])
    app.add_url_rule('/signup',
                        view_func=signup,
                        methods=['POST'])
