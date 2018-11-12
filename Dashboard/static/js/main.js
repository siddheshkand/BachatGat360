function calculate() {
    let total = parseInt($('#tb_1_1').val()) + parseInt($('#tb_1_2').val()) + parseInt($('#tb_1_3').val());
    $('#tb_1_4').val(total);
}

$('#tb_1_1').keyup(function () {
    calculate();
});

$('#tb_1_2').keyup(function () {
    calculate();
});

$('#tb_1_3').keyup(function () {
    calculate();
});

