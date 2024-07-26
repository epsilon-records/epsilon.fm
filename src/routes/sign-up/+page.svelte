<script lang="ts">
	import SignUp from 'clerk-sveltekit/client/SignUp.svelte';
</script>

<div class="container">
	<div class="m-4 self-center">
		<SignUp redirectUrl="/" />
	</div>
</div>

<style>
	.container {
		max-width: 900px;
		padding: 1em;
		display: flex;
		justify-content: center;
	}
</style>
