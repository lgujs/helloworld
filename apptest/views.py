from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from apptest.models import Poll, Choice
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

'''
def poll_index(request):
    polls = Poll.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('apptest/index.html')
    context = Context({'latest_poll_list': polls})
#    response = ', '.join([p.question for p in polls])
#    return HttpResponse(template.render(context))
    return render(request, 'apptest/index.html', context)


def detail(request, poll_id):
    try:
        p = Poll.objects.get(id=poll_id)

    except Poll.DoesNotExist:
        raise Http404()
    return render(request, 'apptest/detail.html', {'poll': p})
#    return HttpResponse("You're looking at poll %s:%s." % (poll_id, p.question))


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'apptest/results.html', {'poll': p})
'''


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    print 'get request:',request.GET
    print 'Post request:', request.POST
    try:
        key = request.POST['choice']
        print 'user select choice %s' %(key,)
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'apptest/detail.html', {'tpoll': p, 'message': "You didnot select a choice."})
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))