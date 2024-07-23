<!-- CommandPalette.svelte -->
<script lang="ts">
	import { Command } from 'cmdk-sv';
	import { onMount, onDestroy } from 'svelte';
	import { writable } from 'svelte/store';

	const open = writable(false);

	function handleKeyDown(event: KeyboardEvent) {
		if (event.metaKey && event.key === 'k') {
			event.preventDefault();
			open.update((value) => !value);
		}
	}

	onMount(() => {
		document.addEventListener('keydown', handleKeyDown);
	});

	onDestroy(() => {
		document.removeEventListener('keydown', handleKeyDown);
	});
</script>

{#if $open}
	<Command.Dialog open={$open} onOpenChange={(value) => open.set(value)}>
		<Command.Input placeholder="Type a command or search..." />
		<Command.List>
			<Command.Item onSelect={() => console.log('Command 1')}>Command 1</Command.Item>
			<Command.Item onSelect={() => console.log('Command 2')}>Command 2</Command.Item>
			<!-- Add more commands as needed -->
		</Command.List>
	</Command.Dialog>
{/if}

<style>
	/* Add your custom styles here */
</style>
