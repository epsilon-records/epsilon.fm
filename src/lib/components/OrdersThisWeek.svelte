<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import { Progress } from '$lib/components/ui/progress/index.js';
</script>

<Card.Root>
	<Card.Header class="pb-2">
		<Card.Description>This Week</Card.Description>
		<Card.Title class="text-4xl">$1329</Card.Title>
	</Card.Header>
	<Card.Content>
		<div class="text-xs text-muted-foreground">+25% from last week</div>
	</Card.Content>
	<Card.Footer>
		<Progress value={25} aria-label="25% increase" />
	</Card.Footer>
</Card.Root>
