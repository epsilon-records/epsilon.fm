<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar/index.js';
</script>

<Menubar.Menu>
	<Menubar.Trigger class="relative">File</Menubar.Trigger>
	<Menubar.Content>
		<Menubar.Sub>
			<Menubar.SubTrigger>New</Menubar.SubTrigger>
			<Menubar.SubContent class="w-[230px]">
				<Menubar.Item>
					Playlist <Menubar.Shortcut>⌘N</Menubar.Shortcut>
				</Menubar.Item>
				<Menubar.Item disabled>
					Playlist from Selection <Menubar.Shortcut>⇧⌘N</Menubar.Shortcut>
				</Menubar.Item>
				<Menubar.Item>
					Smart Playlist... <Menubar.Shortcut>⌥⌘N</Menubar.Shortcut>
				</Menubar.Item>
				<Menubar.Item>Playlist Folder</Menubar.Item>
				<Menubar.Item disabled>Genius Playlist</Menubar.Item>
			</Menubar.SubContent>
		</Menubar.Sub>
		<Menubar.Item>
			Open Stream URL... <Menubar.Shortcut>⌘U</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item>
			Close Window <Menubar.Shortcut>⌘W</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Sub>
			<Menubar.SubTrigger>Library</Menubar.SubTrigger>
			<Menubar.SubContent>
				<Menubar.Item>Update Cloud Library</Menubar.Item>
				<Menubar.Item>Update Genius</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item>Organize Library...</Menubar.Item>
				<Menubar.Item>Export Library...</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item>Import Playlist...</Menubar.Item>
				<Menubar.Item disabled>Export Playlist...</Menubar.Item>
				<Menubar.Item>Show Duplicate Items</Menubar.Item>
				<Menubar.Separator />
				<Menubar.Item>Get Album Artwork</Menubar.Item>
				<Menubar.Item disabled>Get Track Names</Menubar.Item>
			</Menubar.SubContent>
		</Menubar.Sub>
		<Menubar.Item>
			Import... <Menubar.Shortcut>⌘O</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item disabled>Burn Playlist to Disc...</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item>
			Show in Finder <Menubar.Shortcut>⇧⌘R</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item>Convert</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item>Page Setup...</Menubar.Item>
		<Menubar.Item disabled>
			Print... <Menubar.Shortcut>⌘P</Menubar.Shortcut>
		</Menubar.Item>
	</Menubar.Content>
</Menubar.Menu>
