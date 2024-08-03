<script lang="ts">
	import MusicTabs from '$lib/components/MusicTabs.svelte';
	import { playlists } from '$lib/components/(data)/playlists.js';
	import Sidebar from '@/components/Sidebar.svelte';
</script>

<div class="grid border-t bg-background lg:grid-cols-5">
	<Sidebar {playlists} class="hidden lg:block" />
	<div class="col-span-3 h-full px-4 py-6 lg:col-span-4 lg:border-l lg:px-8">
		<MusicTabs></MusicTabs>
	</div>
</div>
