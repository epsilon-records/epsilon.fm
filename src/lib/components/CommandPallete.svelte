<!-- CommandPalette.svelte -->
<script lang="ts">
	import { Command } from 'cmdk-sv';
	import { onMount, onDestroy } from 'svelte';
	import { writable } from 'svelte/store';

	const open = writable(false);

	function onKeyDown(event: KeyboardEvent) {
		if (event.metaKey && event.key === 'k') {
			event.preventDefault();
			open.update((value) => !value);
		}
	}
</script>

{#if $open}
	<Command.Dialog open={$open} onOpenChange={(value) => open.set(value)}>
		<Command.Input placeholder="Type a command or search..." />
		<Command.List>
			<Command.Item onSelect={() => console.log('Command 1')}>Command 1</Command.Item>
			<Command.Item onSelect={() => console.log('Command 2')}>Command 2</Command.Item>
		</Command.List>
	</Command.Dialog>
{/if}

<svelte:window on:keydown|preventDefault={onKeyDown} />
