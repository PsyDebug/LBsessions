function send(var1)
{
$("#myModal").modal('show');
$('#floatingCirclesG').css('display', 'block');
                        $("#histsr").empty();

//alert(var1);
var data = var1;
       $.ajax({ type: "GET",
                url: "/base/hist/",
                data: "search="+data+"",
                // Выводим то что вернул PHP
                success: function(html) {
$('#floatingCirclesG').css('display', 'none');
 //предварительно очищаем нужный элемент страницы
                        $("#histsr").empty();
//и выводим ответ php скрипта
                        $("#histsr").append(html);
                }
        });
}
