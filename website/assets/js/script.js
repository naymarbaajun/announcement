
        function validateForm() {
            var password = document.getElementById("password").value;
            var comfirm = document.getElementById("comfirm").value;

            if (password !== comfirm) {
                alert("passowrd do not match");
                return false;
            }
            alert('wonderful! form submitted');
            return true;

        }
    
    