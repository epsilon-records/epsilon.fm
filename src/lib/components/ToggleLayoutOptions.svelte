<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar';
	import { statusBarVisible } from '$lib/stores/ui';

	function toggleStatusBar() {
		statusBarVisible.update((value) => !value);
	}
</script>

<Menubar.CheckboxItem checked={$statusBarVisible} on:click={toggleStatusBar}>
	{$statusBarVisible ? 'Hide' : 'Show'} Status Bar
	<Menubar.Shortcut>⌘/</Menubar.Shortcut>
</Menubar.CheckboxItem>
<Menubar.CheckboxItem checked disabled>Show Sidebar</Menubar.CheckboxItem>
