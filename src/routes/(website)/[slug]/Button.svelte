<script>
	export let email;
</script>

<div
	class="button"
	role="button"
	tabindex="0"
	on:keypress={() => {
		window.location.href = `mailto:${email}`;
	}}
	on:click={() => {
		window.location.href = `mailto:${email}`;
	}}
>
	<slot />
</div>

<style>
	.button {
		cursor: pointer;
		height: 40px;
		max-width: 200px;
		border-radius: 10px;
		background: #ca3c25;

		background-size: 150% 150%;

		display: flex;
		justify-content: center;
		align-items: center;
		font-weight: 500;
	}

	.button:hover {
		animation: gradient 2s ease infinite;
	}
</style>
