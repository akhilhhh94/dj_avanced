class TitleMixin(object):
    title = None

    def getTitle(self):
        return self.title

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = self.getTitle()
        return context
