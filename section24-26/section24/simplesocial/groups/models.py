from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
import misaka
from django.contrib.auth import get_user_model

User = get_user_model()

from django import template

register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode="True", unique=True)
    description = models.TextField(blank=True, default="")
    description_html = models.TextField(editable=False, default="", blank=True)
    members = models.ManyToManyField(User, through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description_html)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("group:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships")
    user = models.ForeignKey(User, related_name="user_group")

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")


# Lớp Group trong Django là một model đại diện cho một nhóm (group). Dưới đây là giải thích về các trường (fields) và mục đích của chúng:

# name: Là một trường CharField có độ dài tối đa 255 ký tự và được đánh dấu là unique=True. Điều này đảm bảo rằng giá trị của trường name trong mỗi bản ghi của model Group là duy nhất. name là tên của nhóm.

# slug: Là một trường SlugField cho phép sử dụng các ký tự Unicode (allow_unicode=True). Ký tự slug được sử dụng để xây dựng URL thân thiện với người dùng cho nhóm. Khi tạo một nhóm mới, Django sẽ tự động tạo giá trị slug dựa trên giá trị của trường name. Đảm bảo rằng mỗi slug là duy nhất với unique=True.

# description: Là một trường TextField có thể để trống (blank=True) và có giá trị mặc định là một chuỗi trống (default=""). Đây là trường mô tả cho nhóm.

# description_html: Là một trường TextField không thể chỉnh sửa (editable=False), có giá trị mặc định là một chuỗi trống (default="") và có thể để trống (blank=True). Trường description_html dùng để lưu trữ phiên bản đã được xử lý của trường description. Điều này cho phép bạn thực hiện việc xử lý văn bản hoặc tạo mã HTML từ nội dung trường description.

# members: Là một trường ManyToManyField đại diện cho mối quan hệ n-n (nhiều người dùng có thể thuộc nhiều nhóm). Trường này sử dụng User model (hoạt động cùng với get_user_model()) và liên kết qua mô hình GroupMember thông qua thuộc tính through="GroupMember"

# __str__(self): Đây là phương thức ghi đè (override) trong Python, được sử dụng để định nghĩa cách đối tượng của lớp Group sẽ được biểu diễn dưới dạng một chuỗi. Trong trường hợp này, phương thức __str__() trả về tên của nhóm (self.name). Khi sử dụng str() hoặc khi biểu diễn đối tượng Group dưới dạng chuỗi, nó sẽ hiển thị tên của nhóm.

# save(self, *args, **kwargs): Đây là phương thức ghi đè trong Django, được sử dụng để định nghĩa logic lưu trữ khi một đối tượng Group được lưu vào cơ sở dữ liệu. Trong trường hợp này, phương thức save() được mở rộng để thực hiện các công việc sau:


# Gán giá trị slug cho self.slug, sử dụng hàm slugify() để tạo một slug từ self.name. slugify() chuyển đổi chuỗi thành một slug hợp lệ, thường dùng cho các thành phần URL thân thiện với SEO.
# Chuyển đổi nội dung self.description_html thành mã HTML sử dụng misaka.html(), một công cụ xử lý Markdown cho Python.
# Gọi phương thức super().save(*args, **kwargs) để lưu trữ đối tượng Group một cách bình thường.

#    Các tham số *args và **kwargs cho phép phương thức save() nhận các tham số bổ sung.

# get_absolute_url(self): Đây là một phương thức để xác định URL tuyệt đối cho đối tượng Group. Phương thức này sử dụng hàm reverse() để xác định URL của tài nguyên group:single, sử dụng self.slug làm đối số cho thành phần slug trong URL. Khi gọi get_absolute_url() trên một đối tượng Group, nó sẽ trả về URL tuyệt đối để xem chi tiết nhóm.

# class Meta: Đây là một lớp nhúng được sử dụng để cung cấp các thông tin bổ sung về cách các đối tượng Group của bạn được xử lý trong Django. Trong trường hợp này:


# ordering = ["name"] chỉ định rằng các đối tượng Group sẽ được sắp xếp theo trường name. Khi truy vấn dữ liệu từ model Group, các đối tượng sẽ được sắp xếp theo giá trị của trường name.
