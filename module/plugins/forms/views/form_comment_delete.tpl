<script type="text/javascript">
   function submit_local_form() {
      // Launch comments deletion and bailout this modal view
      delete_all_comments('{{name}}');
      // If a comment is to be added ...
      if ($('#comment').val()) {
         add_comment("{{name}}", '{{username}}', $('#comment').val());
      }
      start_refresh();
      $('#modal').modal('hide');
   }
</script>

<div class="modal-dialog">
  <div class="modal-content">
    <div class="modal-header">
      <a class="close" data-dismiss="modal">×</a>
      <h3>Confirm comment(s) deletion</h3>
    </div>

    <div class="modal-body">
      <form name="input_form" role="form">
        <div class="form-group">
          <textarea name="reason" id="reason" class="form-control" rows="5" placeholder="Comment…">All comments deleted for {{name}} by {{user.get_name()}}.</textarea>
        </div>
        
        <a href="javascript:submit_local_form();" class="btn btn-danger btn-lg btn-block"> <i class="fa fa-save"></i> Submit</a>
      </form>
    </div>
  </div>
</div>
