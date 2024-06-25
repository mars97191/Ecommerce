

from product.models import Wishlist
from users.models import User


def default(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
        return {'wishlist': wishlist}
    else:
        return {}