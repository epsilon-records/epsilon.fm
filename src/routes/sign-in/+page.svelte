<script lang="ts">
	import SignIn from 'clerk-sveltekit/client/SignIn.svelte';
</script>

<div class="container">
	<div class="m-4 self-center">
		<SignIn redirectUrl="/" />
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
