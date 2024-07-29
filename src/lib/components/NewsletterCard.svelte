<script lang="ts">
	import ConvertKit from '$lib/components/ConvertKit.svelte';
	import * as Card from '$lib/components/ui/card';
</script>

<Card.Root class="m-4 w-3/5 max-w-xl">
	<Card.Header>
		<div class="flex items-center justify-center">
			<p class="font-mono text-2xl">Join our Newsletter</p>
		</div>
	</Card.Header>
	<Card.Content>
		<ConvertKit></ConvertKit>
	</Card.Content>
</Card.Root>
