<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar';
	import { statusBarVisible, sidebarVisible } from '$lib/stores/ui';

	function toggleStatusBar() {
		statusBarVisible.update((value) => !value);
	}

	function toggleSideBar() {
		sidebarVisible.update((value) => !value);
	}
</script>

<Menubar.CheckboxItem checked={$statusBarVisible} on:click={toggleStatusBar}>
	{$statusBarVisible ? 'Hide' : 'Show'} Status Bar
	<Menubar.Shortcut>⌘/</Menubar.Shortcut>
</Menubar.CheckboxItem>
<Menubar.CheckboxItem checked={$sidebarVisible} on:click={toggleSideBar}>
	{$sidebarVisible ? 'Hide' : 'Show'} Sidebar
	<Menubar.Shortcut>⌘\</Menubar.Shortcut>
</Menubar.CheckboxItem>
