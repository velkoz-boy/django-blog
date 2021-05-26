from django.views import generic


class ProfileView(generic.TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["disable_category"] = True
        return context
