<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';

	export let firstName: string;

	function getGreeting(): string {
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

<Card.Root class="sm:col-span-2">
	<Card.Header class="pb-3">
		<Card.Title>{getGreeting()}</Card.Title>
		<Card.Description class="max-w-lg text-balance leading-relaxed">
			Introducing our new Release Dashboard, designed for easy management and detailed analysis.
		</Card.Description>
	</Card.Header>
	<Card.Footer>
		<Button>Create New Release</Button>
	</Card.Footer>
</Card.Root>
