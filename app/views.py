import json
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from app.models import Entry, Log


class Index(ListView):
    model = Entry
    template_name = 'index.html'
    paginate_by = 500

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['pages_range'] = range(1, context['page_obj'].paginator.num_pages + 1)
        return context


class EntryCreate(CreateView):
    model = Entry
    template_name = 'entry/create.html'
    success_url = reverse_lazy('index')


class EntryUpdate(UpdateView):
    model = Entry
    template_name = 'entry/update.html'
    success_url = reverse_lazy('index')


class EntryDelete(DeleteView):
    model = Entry
    success_url = reverse_lazy('index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class LogList(ListView):
    model = Log
    template_name = 'log/log.html'
    paginate_by = 500
    default_sort_field = 'datetime'

    def get_queryset(self):
        q = self.request.GET.get('term')
        if q:
            return Log.objects.filter(text__icontains=q).order_by("datetime").reverse()
        return super(LogList, self).get_queryset().order_by("datetime").reverse()

    def get_context_data(self, *args, **kwargs):
        context = super(LogList, self).get_context_data(**kwargs)
        context['pages_range'] = range(1, context['page_obj'].paginator.num_pages + 1)
        return context


def search_entries(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        if q.isdigit():
            entries = list(Entry.objects.filter(Q(number__contains=q) | Q(text__contains=q)))[:10]
        else:
            entries = list(Entry.objects.filter(text__contains=q))[:10]
        response = []
        for entry in entries:
            label = "%s - %d" % (entry.text, entry.number)
            entry_item = {'id': entry.id, 'label': label, 'number': entry.number}
            response.append(entry_item)
        data = json.dumps(response)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)