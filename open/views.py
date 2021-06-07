from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,DetailView,
                                  ListView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from open.models import Story,Review
from open.forms import StoryForm,ReviewForm
from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = 'open/index.html'

class StoryListView(ListView):
    model = Story

    def get_queryset(self):
        return Story.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class StoryDetailView(DetailView):
    model = Story

class StoryCreateView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'open/story_detail.html'

    form_class = StoryForm
    model = Story


class StoryUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'open/story_detail.html'

    form_class = StoryForm
    model = Story

class StoryDeleteView(DeleteView,LoginRequiredMixin):
    model = Story
    success_url = reverse_lazy('open:story_list')

class DraftListView(ListView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'open/story_draft_list.html'
    model = Story

    def get_queryset(self):
        return Story.objects.filter(publish_date__isnull=True).order_by('creation_date')

@login_required
def add_review_to_story(request,pk):
    story = get_object_or_404(Story,pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.story = story
            review.save()
            return redirect('open:story_detail',pk=story.pk)
    else:
        form = ReviewForm()
    return render(request,'open/review_form.html',{'form':form})

@login_required
def story_publish(request,pk):
    story = get_object_or_404(Story,pk=pk)
    story.publish()
    return redirect('open:story_detail',pk=story.pk)

@login_required
def review_approval(request,pk):
    review = get_object_or_404(Review,pk=pk)
    review.approve_review()
    return redirect('open:story_detail',pk=review.story.pk)

@login_required
def review_deletion(request,pk):
    review = get_object_or_404(Review,pk=pk)
    storypk = review.story.pk
    review.delete()
    return redirect('open:story_detail',pk=storypk)
