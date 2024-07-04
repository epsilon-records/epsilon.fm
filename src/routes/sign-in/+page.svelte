<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import SignIn from 'clerk-sveltekit/client/SignIn.svelte';
</script>

<div>
	<Card.Root class="m-4">
		<SignIn redirectUrl="/" />
	</Card.Root>
</div>
