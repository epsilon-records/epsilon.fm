<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar/index.js';
	import { goto } from '$app/navigation';
</script>

<Menubar.Menu>
	<Menubar.Trigger class="font-bold">Epsilon FM</Menubar.Trigger>
	<Menubar.Content>
		<Menubar.Item on:click={() => goto('/')}>About Epsilon FM</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item>
			Preferences... <Menubar.Shortcut>⌘,</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Separator />
		<Menubar.Item>
			Hide Music... <Menubar.Shortcut>⌘H</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Item>
			Hide Others... <Menubar.Shortcut>⇧⌘H</Menubar.Shortcut>
		</Menubar.Item>
		<Menubar.Shortcut />
		<Menubar.Item>
			Quit Music <Menubar.Shortcut>⌘Q</Menubar.Shortcut>
		</Menubar.Item>
	</Menubar.Content>
</Menubar.Menu>
