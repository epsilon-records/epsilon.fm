<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import SignUp from 'clerk-sveltekit/client/SignUp.svelte';
</script>

<div>
	<Card.Root class="m-4 content-center">
		<SignUp redirectUrl="/" />
	</Card.Root>
</div>
