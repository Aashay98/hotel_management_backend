# def configure(app):
#     app.add_url_rule('/guest/login',
#                         view_func=retrieve_all_movie_data,
#                         methods=['POST'])
#     app.add_url_rule('/staff/login',
#                         view_func=retrieve_all_movie_data,
#                         methods=['POST'])
#     app.add_url_rule('/guest/change_password',
#                         view_func=retrieve_all_movie_data,
#                         methods=['POST'])
#     app.add_url_rule('/staff/change_password',
#                         view_func=retrieve_movie_data_by_title,
#                         methods=['POST'])
#     app.add_url_rule('/guest/reset_password',
#                         view_func=update_movie_data,
#                         methods=['POST'])
#     app.add_url_rule('/staff/reset_password',
#                         view_func=update_movie_data,
#                         methods=['POST'])
