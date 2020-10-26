from django.shortcuts import render
from .models import Photo
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

#class형 뷰에서 여러개의 객체는 object_list이고, 한 개의 객체는 object / model의 str메서드도 같이나옴
def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})
                                        #object_list인데 변경가능 함 / 위에서 설정한 변수
class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    # 글쓰기 누르면 나오는 것들 사진, 텍스트, (업로드시간, 작성자 필요함)
    template_name = 'photo/upload.html'
    # 업로드시간은 모델에서 설정했기때문에 안해도 됨
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        # form은 author가 필수라 먼저 설정함 / 요청받은 유저 아이디(로그인한 본인)
        if form.is_valid(): #위에서 설정한 폼이 정상이면 그대로 저장한다.
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})
            #설정값에 오류나오면 다시 폼으로 돌려준다. 입력하던 값 잃어버리지 않게


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'
