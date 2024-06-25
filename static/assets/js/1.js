$(document).ready(function () {
    // Обработка добавления в корзину на главной странице
    $(document).on('click', '.add-button', function (e) {
        e.preventDefault();

        // Значение по умолчанию для количества товара
        const productQty = 1;

        // Получаем id продукта из значения кнопки
        const productId = $(this).val();
        console.log("Product ID:", productId);

        // Получаем CSRF токен из скрытого поля
        const csrfToken = $('#csrf_token').val();
        console.log("CSRF Token:", csrfToken);

        // Получаем URL для добавления в корзину из data атрибута
        const addToCartUrl = $(this).data('add-to-cart-url');
        console.log("Add to Cart URL:", addToCartUrl);

        // Сохраняем текущую кнопку для изменения ее текста позже
        const addButton = $(this);
        console.log("Add Button:", addButton);

        $.ajax({
            type: 'POST',
            url: addToCartUrl,  // Используем URL из data атрибута
            data: {
                product_id: productId,
                product_qty: productQty,
                csrfmiddlewaretoken: csrfToken,
                action: 'post'
            },
            success: function (response) {
                console.log("AJAX Success:", response); // Проверяем ответ от сервера

                // Обновляем количество товаров в корзине
                if (response.qty !== undefined) {
                    document.getElementById('lblCartCount').textContent = response.qty;
                } else {
                    console.error('Unexpected response format:', response);
                }

                // Изменяем состояние кнопки
                addButton.prop('disabled', true);
                addButton.text("Товар добавлен");
                addButton.removeClass('btn-secondary').addClass('btn-success');
                console.log("Button Updated:", addButton);
            },
            error: function (error) {
                console.log("AJAX Error:", error); // Проверяем ошибки
                alert('Произошла ошибка при добавлении товара в корзину.');
            }
        });
    });
});


  // Обработка добавления в корзину на странице с подробной информацией о продукте
        $(document).on('click', '#add-to-cart-detail', function (e) {
            e.preventDefault();

            // Получаем выбранное количество продукта
            const productQty = $('#product-quantity').val();

            // Получаем id продукта из значения кнопки
            const productId = $(this).val();

            // Получаем CSRF токен из скрытого поля
            const csrfToken = $('#csrf_token').val();

            $.ajax({
                type: 'POST',
                url: '{% url "cart:add-to-cart" %}',  // Убедитесь, что URL правильный
                data: {
                    product_id: productId,
                    product_qty: productQty,
                    csrfmiddlewaretoken: csrfToken,
                    action: 'post'
                },
                success: function (response) {
                    console.log(response); // Проверяем ответ от сервера

                    // Обновляем количество товаров в корзине
                    if (response.qty !== undefined) {
                        document.getElementById('lblCartCount').textContent = response.qty;
                    } else {
                        console.error('Unexpected response format:', response);
                    }

                    // Изменяем состояние кнопки
                    const addButton = document.getElementById('add-to-cart-detail');
                    addButton.disabled = true;
                    addButton.innerText = "Added to cart";
                    addButton.className = "btn btn-success btn-sm";
                },
                error: function (error) {
                    console.log(error); // Проверяем ошибки
                    alert('An error occurred while adding the product to the cart.');
                }
            });
        });