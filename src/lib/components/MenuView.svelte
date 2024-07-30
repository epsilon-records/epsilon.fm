<script lang="ts">
	import ToggleLayout from './ToggleLayout.svelte';
	import QuickNavigate from './QuickNavigate.svelte';
	import ToggleFullScreen from './ToggleFullScreen.svelte';
	import * as Menubar from '$lib/components/ui/menubar/index';
	import { goto } from '$app/navigation';

	const items = ['dashboard', 'music', 'orders', 'products', 'customers', 'analytics'];

	let isFullScreen = false;

	function toggleFullScreen() {
		if (!document.fullscreenElement) {
			document.documentElement.requestFullscreen();
			isFullScreen = true;
		} else {
			if (document.exitFullscreen) {
				document.exitFullscreen();
				isFullScreen = false;
			}
		}
	}

	function handleKeydown(event: KeyboardEvent) {
		if (!event.metaKey) return;
		if (event.key === 'f') {
			event.preventDefault();
			toggleFullScreen();
		} else {
			const key = parseInt(event.key);
			if (!isNaN(key) && key > 0 && key <= items.length) {
				event.preventDefault();
				goto(`/${items[key - 1]}`);
			}
		}
	}
</script>

<svelte:window on:keydown={handleKeydown} />

<Menubar.Menu>
	<Menubar.Trigger>View</Menubar.Trigger>
	<Menubar.Content>
		<QuickNavigate />
		<Menubar.Separator />
		<Menubar.Separator />
		<ToggleLayout></ToggleLayout>
		<Menubar.Separator />
		<ToggleFullScreen />
	</Menubar.Content>
</Menubar.Menu>
