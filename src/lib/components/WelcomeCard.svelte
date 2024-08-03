<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as Card from '$lib/components/ui/card';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';

	function getGreeting(firstName: string | null | undefined): string {
		const hour = new Date().getHours();
		let greeting = '';

		if (hour < 12) {
			greeting = 'Good morning';
		} else if (hour < 18) {
			greeting = 'Good afternoon';
		} else {
			greeting = 'Good evening';
		}

		return firstName ? `${greeting}, ${firstName}` : greeting;
	}
</script>

<SignedIn let:user>
	<Card.Root class="sm:col-span-2">
		<Card.Header class="pb-3">
			<Card.Title class="text-4xl">{getGreeting(user?.firstName)}</Card.Title>
			<Card.Description class="max-w-lg text-balance leading-relaxed">
				Welcome back 👋
			</Card.Description>
		</Card.Header>
		<Card.Footer>
			<Button>Create New Release</Button>
		</Card.Footer>
	</Card.Root>
</SignedIn>
