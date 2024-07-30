<script lang="ts">
	import ToggleLayout from './ToggleLayout.svelte';
	import QuickNavigate from './QuickNavigate.svelte';
	import ToggleFullScreen from './ToggleFullScreen.svelte';
	import * as Menubar from '$lib/components/ui/menubar/index';
</script>

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
