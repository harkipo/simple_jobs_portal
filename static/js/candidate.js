$("body").on('click',".ms_apply_jobs", function () {

        
   
    console.log('checkbox checked');

    let count = $(`.ms_apply_jobs:checked`).length
    console.log("count is >>>", count);
    $(`.check_count`).html(`${count}`);

    if (count > 0) {
        $(`#multi_job_select_div`).fadeIn();
    } else {
        $(`#multi_job_select_div`).fadeOut();

    }

});
