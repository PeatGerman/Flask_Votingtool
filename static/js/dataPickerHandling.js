function initializeDatePicker() {
    $('#calendar_day').datepicker({
        format: 'dd/mm/yyyy',
        autoclose: true,
        todayHighlight: true,
        orientation: "bottom auto",
        startDate: "today",
        endDate: "+1y",
        clearBtn: true,
        todayBtn: true,
        forceParse: false,
        daysOfWeekDisabled: [0, 6], // Blockiert Sonntag und Samstag
        showWeekNumbers: true,
        language: 'de'
    });

    document.getElementById('datePickerButton').addEventListener('click', function() {
        document.getElementById('calendar_day').focus();
    });
}

document.addEventListener('DOMContentLoaded', initializeDatePicker);
