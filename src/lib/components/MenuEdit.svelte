<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar/index.js';
</script>

<Menubar.Menu>
	<Menubar.Trigger>Edit</Menubar.Trigger>
	<Menubar.Content>
		<Menubar.Item disabled>
			Undo <Menubar.Shortcut>⌘Z</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item disabled>
			Redo <Menubar.Shortcut>⇧⌘Z</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item disabled>
			Cut <Menubar.Shortcut>⌘X</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item disabled>
			Copy <Menubar.Shortcut>⌘C</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item disabled>
			Paste <Menubar.Shortcut>⌘V</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item>
			Select All <Menubar.Shortcut>⌘A</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item disabled>
			Deselect All <Menubar.Shortcut>⇧⌘A</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item>
			Smart Dictation...
			<Menubar.Shortcut>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					stroke="currentColor"
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					class="h-4 w-4"
					viewBox="0 0 24 24"
				>
					<path d="m12 8-9.04 9.06a2.82 2.82 0 1 0 3.98 3.98L16 12" />
					<circle cx="17" cy="7" r="5" />
				</svg>
			</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item>
			Emoji & Symbols
			<Menubar.Shortcut>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					stroke="currentColor"
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					class="h-4 w-4"
					viewBox="0 0 24 24"
				>
					<circle cx="12" cy="12" r="10" />
					<path
						d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
					/>
				</svg>
			</Menubar.Shortcut>
		</Menubar.Item>
	</Menubar.Content>
</Menubar.Menu>
