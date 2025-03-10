class SEOMixin:
    def post(self, request, *arg, **kwargs):
        super().post(request, *arg, **kwargs)
        print("process The query")
        return "Search result and redirection"
    
class View:
    def post(self, request, *arg, **kwargs):
        print("processing Post request!")


class AdminDashboard(SEOMixin, View):
    def get(self, request):
        print("process Get request")
        
class UserView(SEOMixin, View):
    def get(self, request):
        print("process Get request")


print(AdminDashboard().post("Post, Request"), "\n")
print(UserView().post("Post, Request"), "\n")