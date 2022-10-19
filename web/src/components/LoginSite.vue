<script setup>
defineProps({
    name: {
        type: String,
        required: true
    }
})
</script>

<template lang="pug">
.login
    h1.name_color {{name}} 
    .login_form 
        h2.logincolor 
        form
            .input-form
                span User_Code
                input(type="text")
            .input-form
                input(type="submit" value="Confirm")
            .input-form
                p You don't have account? <a href="#">Register</a>
</template>

<style lang="scss" scoped>
.login{
	justify-content: center;
	text-align: center;
	place-items: center;
	.login_form {
		left: 50%;
		background-color: white;
		border-radius: 0.5rem;
		width: 350px;
		justify-content: center;
		align-items: center;
		height: 100%;
		margin: 0 auto;
		border: 1px solid black;
		span {
			font-size: 16px;
			margin: 0 1rem 5px 0;
			display: inline-block;
			color: black;
			letter-spacing: 1px;
		}
		input {
			width: 50%;
			padding: 10px 20px;
			outline: none;
			border: 1px solid #607d8b;
			font-size: 16px;
			letter-spacing: 1px;
			color: #607d8b;
			background: transparent;
			border-radius: 30px;
			margin-bottom: 1.5rem;
		}
	}
	.logincolor {
		color: black;
		font-weight: 500;
		font-size: 1.5em;
		text-transform: uppercase;
		margin-bottom: 20px;
		border-bottom: 4px solid #ff4584;
		display: inline-block;
		letter-spacing: 1px;
	}
	.input-form {
		input[type="submit"] {
			background: #ff4584;
			color: #fff;
			outline: none;
			border: none;
			font-weight: 500;
			cursor: pointer;
			box-shadow: 0 1px 1px rgba(0,0,0,0.12), 0 2px 2px rgba(0,0,0,0.12), 0 4px 4px rgba(0,0,0,0.12), 0 8px 8px rgba(0,0,0,0.12), 0 16px 16px rgba(0,0,0,0.12);
			width: 50%;
			&:hover {
				background: #f53677;
			}
		}
		p {
			color: #607d8b;
		}
	}
	section {
		.noi-dung {
			.form {
				.input-form {
					p {
						a {
							color: #ff4584;
						}
					}
				}
			}
		}
	}
}



</style>