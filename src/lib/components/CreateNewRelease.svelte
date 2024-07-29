<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
</script>

<Card.Root class="sm:col-span-2">
	<Card.Header class="pb-3">
		<Card.Title>Your Releases</Card.Title>
		<Card.Description class="max-w-lg text-balance leading-relaxed">
			Introducing Our Dynamic Release Dashboard for Seamless Management and Insightful Analysis.
		</Card.Description>
	</Card.Header>
	<Card.Footer>
		<Button>Create New Release</Button>
	</Card.Footer>
</Card.Root>
