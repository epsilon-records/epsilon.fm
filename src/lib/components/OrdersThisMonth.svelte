<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import { Progress } from '$lib/components/ui/progress/index.js';
</script>

<Card.Root class="sm:col-span-1">
	<Card.Header class="pb-2">
		<Card.Description>This Month</Card.Description>
		<Card.Title class="text-3xl">$5,329</Card.Title>
	</Card.Header>
	<Card.Content>
		<div class="text-xs text-muted-foreground">+10% from last month</div>
	</Card.Content>
	<Card.Footer>
		<Progress value={12} aria-label="12% increase" />
	</Card.Footer>
</Card.Root>
