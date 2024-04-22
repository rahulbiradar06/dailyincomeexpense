def check_first_middleware(get_response):
    print('this code one time')
    print('this code one time')
    print('this code one time')

    def data(request):
        print('========this  fun executes before request========')

        print('executes before view app========')


        response=get_response(request)
        print('========this fun executes after request========')

        return response
    
    return data