import random
import os


class Name():
    special_suffixes = {
        "kitten": "kit",
        "apprentice": "paw",
        "medicine cat apprentice": "paw",
        "leader": "star"
    }
    normal_suffixes = [  # common suffixes
        "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", 'fur', 'fur', 'fur',
        'pelt', "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "claw", "claw", "claw", "claw", "claw", "claw", "claw",
        "foot","foot", "foot","foot", "foot", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", 'heart',

        # regular suffixes
        "acorn", "ash", "aster", "back", "beam", "bee", "belly", "berry", "bite", "bird", "blaze", "blink",
        "blossom", "bloom", "blotch", "bounce", "branch", "breeze", "briar", "bright", "brook", "burr", "bush",
        "call", "cloud", "clover", "coral", "creek", "cry", "dapple", "daisy", "dawn", "drift", "drop",
        "dusk", "dust", "ear", "ears", "eye", "eyes", "face", "fall", "fang", "feather", "fern", "fin", "fire",
        "fish", "flame", "flight", "flood", "flower", "frost", "gaze", "goose", "gorse", "grass", "hail", "hare", 
        "hawk", "haze", "heather", "holly", "hollow", "ivy", "jaw", "jay", "jump", "kite",
        "lake", "larch", "leaf", "leap", "leg", "light", "lilac", "lily", "lotus", "mask", "mist", "moth",
        "moon", "mouse", "needle", "nettle", "night", "noise", "nose", "nut", "pad", "path", "patch",
        "petal", "pond", "pool", "poppy", "pounce", "puddle", "rapid", "rose", "rump", "run", "runner",
        "scar", "seed", "shade", "shadow", "shell", "shine", "sight", "skip", "sky", "slip", "snow", "song", 
        "spark", "speck", "speckle", "spirit", "splash", "spot", "spots", "spring", "stalk", "stem", "step",
        "stone", "storm", "streak", "stream", "strike", "stripe", "sun", "swipe", "swoop",
        "tail", "tree", "throat", "tuft", "watcher", "water", "whisper", "willow", "wind", "wing", "wish"
        'adder', 'alder', 'amble', 'ant', 'antler', 'apple', 'apricot', 'arc', 'arch', 'aspen', 'badger', 'bark',
        'barley', 'bat', 'bay', 'beaver', 'beech', 'beetle', 'belladonna', 'beyond', 'birch', 'blizzard', 'bog',
        'bolt', 'borage', 'bough', 'boulder', 'bound', 'bracken', 'bramble', 'bristle', 'brush', 'buck', 'bug',
        'bumble', 'burdock', 'burn', 'burrow', 'bush', 'buzzard', 'carp', 'catch', 'catcher', 'cedar',
        'char', 'charge', 'chatter', 'cheetah', 'cherry', 'chestnut', 'chive', 'cinder', 'cinnamon', 'clematis',
        'clue', 'cone', 'cress', 'cricket', 'crouch', 'crow', 'curl', 'cypress', 'dance', 'damp', 'dark', 'dash',
        'deer', 'dew', 'ditch', 'doe', 'dog', 'dots', 'dove', 'down', 'dream', 'dreamer', 'dry', 'duck', 'eagle',
        'echo', 'eel', 'elm', 'ember', 'ermine', 'fade', 'fallow', 'fawn', 'fennel', 'ferret', 'finch', 'fir', 'fisher',
        'flake', 'flail', 'flare', 'flash', 'flax', 'flicker', 'flint', 'flip', 'flutter', 'fly', 'fog', 'fox', 'freckle', 'freckles',
        'freeze', 'frog', 'frond', 'fur', 'fuzz', 'gleam', 'glide', 'glimmer', 'glow', 'gravel', 'ground',
        'gull', 'half', 'hare', 'harrier', 'hatch', 'hay', 'hedge', 'hemlock', 'heron', 'hickory', 'hill', 'hills',
        'honey', 'hoot', 'hop', 'hope', 'hopper', 'horse', 'hound', 'hunter', 'ice', 'inferno', 'jackdaw', 'jumper',
        'kestrel', 'kindle', 'knap', 'land', 'lantana', 'lark', 'larkspur', 'laurel', 'lavender', 'leaper', 'lemon', 'leopard',
        'lichen', 'lightning', 'lime', 'lion', 'lizard', 'log', 'lunge', 'lynx', 'maggot', 'mallow', 'maple', 'march', 'marcher',
        'marigold', 'marsh', 'martin', 'meadow', 'midge', 'milk', 'minnow', 'mint', 'mistle', 'mole', 'morning', 'moss',
        'mottle', 'moose', 'mud', 'mumble', 'murmur', 'nectar', 'nightshade', 'newt', 'oak', 'oat', 'oleander', 'olive', 'orange',
        'otter', 'owl', 'panther', 'parsley', 'patches', 'peak', 'pear', 'peat', 'pebble', 'peony', 'perch', 'pheasant', 'pigeon', 'pike',
        'pine', 'plum', 'pod', 'prance', 'prickle', 'primrose', 'python', 'quail', 'rabbit', 'rain', 'rat', 'raven', 'reed', 'ridge',
        'ripple', 'rise', 'river', 'roar', 'robin', 'rock', 'rook', 'root', 'rover', 'rowan', 'rubble', 'rush', 'rusher', 'rust', 'rye', 'sage',
        'salmon', 'sand', 'scamper', 'scorch', 'scramble', 'scuttle', 'sedge', 'seer', 'sheep', 'shimmer', 'shine', 'shrew', 'shy',
        'silence', 'silt', 'skitter', 'slate', 'sleet', 'sloe', 'slope', 'smoke', 'snail', 'snake', 'snap', 'snapper', 'snarl', 'sneeze', 'snip',
        'snout', 'soot', 'sorrel', 'sparrow', 'speckles', 'specks', 'spider', 'spike', 'spire', 'sprint', 'sprout', 'spruce', 'squirrel', 'stag',
        'starling', 'stoat', 'stride', 'stork', 'stump', 'swallow', 'swamp', 'swan', 'sweet', 'swift', 'swirl', 'talon', 'tear', 'thicket', 'thistle',
        'thrift', 'thorn', 'thunder', 'thyme', 'tiger', 'timber', 'tip', 'toe', 'torrent', 'tooth', 'trail', 'traipse', 'travel', 'traveler', 'trot', 'trout',
        'tulip', 'tumble', 'turtle', 'tussock', 'twig', 'twirl', 'vine', 'violet', 'vixen', 'vole', 'walk', 'walker', 'wander', 'wanderer', 'wasp',
        'warren', 'water', 'weasel', 'weed', 'wheat', 'whistle', 'whistler', 'wiggle', 'wither', 'wonder', 'wood', 'wort', 'wound',
        'wounder', 'wren', 'yarrow', 'yew', 'yonder', 'zinnia' 
    ]

    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Tabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Marbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Speckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Bengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'Tortie': ['dapple', 'speckle', 'spot', 'dapple'],
        'Rosette': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch'],
        'Smoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'Ticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Abyssinian': ['fade', 'dusk', 'dawn', 'smoke'],
        'Merle': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'dog', 'hound'],
        'Clouded': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Snowflake': ['dapple', 'speckle', 'spot', 'speck', 'freckle', 'snow', 'snowflake'],
        'Doberman': ['patch', 'spot', 'splash', 'patch', 'spots', 'hound', 'dog'],
        'Ghost': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'ghost'],
        'Pinstripe': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Spotted': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Cloudy': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Classic': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Mackerel': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Sokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Gradient': ['fade', 'dusk', 'dawn', 'smoke'],
        'Siamese': ['fade', 'dusk', 'dawn', 'smoke'],
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortietabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiebengal': ['dapple', 'speckle', 'spots', 'speck', 'fern', 'freckle'],
        'tortiemarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortieticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'tortiesmoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'tortierosette': ['dapple', 'speckle', 'spots', 'dapple', 'fern', 'freckle'],
        'tortiespeckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortiemerle': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'dog', 'hound'],
        'tortieclouded': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'tortiesnowflake': ['dapple', 'speckle', 'spot', 'speck', 'freckle', 'snow', 'snowflake'],
        'tortieghost': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'ghost'],
        'tortiepinstripe': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'tortieclassic': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiemackerel': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiesokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern']
    }

    normal_prefixes = [
        'Acacia', 'Acorn', 'Adder', 'Alder', 'Algae', 'Almond', 'Aloe',
        'Amber', 'Ant', 'Antler', 'Apple', 'Apricot', 'Arc', 'Arch', 'Arctic',
        'Ash', 'Ashen', 'Aspen', 'Aster', 'Aster', 'Autumn', 'Badger', 'Bark',
        'Barley', 'Barley', 'Basil', 'Bass', 'Bat', 'Bay', 'Bayou', 'Beam',
        'Bear', 'Beaver', 'Bee', 'Beech', 'Beetle', 'Berry', 'Big', 'Birch',
        'Bird', 'Bite', 'Bitter', 'Bittern', 'Blaze', 'Bleak', 'Blight',
        'Blink', 'Bliss', 'Bloom', 'Blossom', 'Blotch', 'Bluff', 'Bog', 'Bog',
        'Bold', 'Borage', 'Bough', 'Boulder', 'Bounce', 'Bracken', 'Bramble',
        'Branch', 'Brave', 'Breeze', 'Breeze', 'Briar', 'Bright', 'Brindle',
        'Bristle', 'Broken', 'Brook', 'Brush', 'Bubble', 'Bubbling', 'Buck',
        'Bug', 'Bumble', 'Burdock', 'Burn', 'Burnt', 'Burr', 'Bush', 'Buzzard',
        'Carp', 'Cedar', 'Cedar', 'Chaffinch', 'Char', 'Cheetah', 'Cherry',
        'Chestnut', 'Chive', 'Cicada', 'Cinder', 'Cinnamon', 'Claw', 'Clay',
        'Cliff', 'Cloud', 'Clover', 'Clover', 'Coast', 'Cobra', 'Cod', 'Cold',
        'Condor', 'Cone', 'Conifer', 'Copper', 'Cotton', 'Cougar', 'Cow',
        'Coyote', 'Crab', 'Crag', 'Crane', 'Creek', 'Cress', 'Crested',
        'Cricket', 'Crooked', 'Crouch', 'Crow', 'Crow', 'Curl', 'Curlew',
        'Curly', 'Cypress', 'Dahlia', 'Daisy', 'Damp', 'Dapple', 'Dappled',
        'Dark', 'Dawn', 'Dawn', 'Day', 'Dead', 'Deer', 'Dew', 'Doe', 'Dog',
        'Dove', 'Down', 'Downy', 'Drake', 'Drift', 'Drizzle', 'Drought', 'Dry',
        'Duck', 'Dull', 'Dune', 'Dusk', 'Dust', 'Eagle', 'Echo', 'Eel',
        'Egret', 'Elk', 'Elm', 'Ember', 'Ermine', 'Faded', 'Faded', 'Fading',
        'Falcon', 'Fallen', 'Fallen', 'Fallow', 'Fawn', 'Feather', 'Fennel',
        'Fern', 'Ferret', 'Fidget', 'Fierce', 'Fin', 'Finch', 'Fir', 'Fish',
        'Flail', 'Flame', 'Flash', 'Flax', 'Fleck', 'Fleet', 'Flicker',
        'Flight', 'Flint', 'Flip', 'Flood', 'Flood', 'Flower', 'Flower',
        'Flurry', 'Flutter', 'Fly', 'Foam', 'Forest', 'Fox', 'Freckle',
        'Freeze', 'Fringe', 'Frog', 'Frond', 'Frost', 'Frozen', 'Furled',
        'Fuzzy', 'Gander', 'Gannet', 'Gem', 'Giant', 'Gill', 'Gleam', 'Glow',
        'Goose', 'Gorge', 'Gorse', 'Grass', 'Gravel', 'Grouse', 'Gull', 'Gust',
        'Hail', 'Half', 'Hare', 'Harvest', 'Hatch', 'Hawk', 'Hay', 'Haze',
        'Heath', 'Heather', 'Heavy', 'Hedge', 'Hen', 'Heron', 'Hickory',
        'Hill', 'Hoarse', 'Hollow', 'Holly', 'Hoot', 'Hop', 'Hope', 'Hornet',
        'Hound', 'Ice', 'Icy', 'Iris', 'Ivy', 'Jagged', 'Jasper', 'Jay', 'Jet',
        'Jump', 'Juniper', 'Kestrel', 'Kink', 'Kite', 'Lake', 'Larch', 'Lark',
        'Laurel', 'Lavender', 'Leaf', 'Leap', 'Leopard', 'Lichen', 'Light',
        'Lightning', 'Lilac', 'Lilac', 'Lily', 'Little', 'Lizard', 'Locust',
        'Log', 'Long', 'Lost', 'Lotus', 'Loud', 'Low', 'Lynx', 'Maggot',
        'Mallow', 'Mantis', 'Maple', 'Marigold', 'Marsh', 'Marten', 'Meadow',
        'Mellow', 'Merry', 'Midge', 'Milk', 'Mink', 'Minnow', 'Mint', 'Mist',
        'Mistle', 'Misty', 'Mite', 'Mock', 'Mole', 'Mole', 'Moon', 'Moor',
        'Morning', 'Moss', 'Mossy', 'Moth', 'Moth', 'Mottle', 'Mottled',
        'Mouse', 'Mouse', 'Mud', 'Mumble', 'Murk', 'Nacre', 'Narrow', 'Nectar',
        'Needle', 'Nettle', 'Newt', 'Night', 'Nut', 'Oak', 'Oat', 'Odd', 'One',
        'Orange', 'Osprey', 'Otter', 'Owl', 'Pale', 'Pansy', 'Panther',
        'Parsley', 'Partridge', 'Patch', 'Peak', 'Pear', 'Peat', 'Peat',
        'Pebble', 'Pepper', 'Perch', 'Petal', 'Pheasant', 'Pigeon', 'Pike',
        'Pine', 'Piper', 'Plover', 'Pod', 'Pond', 'Pool', 'Poppy', 'Posy',
        'Pounce', 'Prance', 'Prickle', 'Prim', 'Puddle', 'Python', 'Quail',
        'Quick', 'Quiet', 'Quill', 'Rabbit', 'Raccoon', 'Ragged', 'Rain',
        'Rambling', 'Rat', 'Rattle', 'Raven', 'Reed', 'Ridge', 'Rift',
        'Ripple', 'River', 'Roach', 'Robin', 'Rock', 'Rook', 'Root', 'Rose',
        'Rosy', 'Rot', 'Rowan', 'Rubble', 'Running', 'Rush', 'Rust', 'Rye',
        'Sage', 'Sandy', 'Scar', 'Scorch', 'Sea', 'Sedge', 'Seed', 'Shade',
        'Shard', 'Sharp', 'Shell', 'Shimmer', 'Short', 'Shrew', 'Shy', 'Silk',
        'Silt', 'Skip', 'Sky', 'Slate', 'Sleek', 'Sleet', 'Slight', 'Sloe',
        'Slope', 'Small', 'Smoke', 'Smoky', 'Snail', 'Snake', 'Snap', 'Sneeze',
        'Snip', 'Soft', 'Song', 'Soot', 'Sorrel', 'Spark', 'Sparrow',
        'Speckle', 'Spider', 'Spike', 'Spire', 'Splash', 'Spotted', 'Spring',
        'Spruce', 'Squirrel', 'Stag', 'Starling', 'Steam', 'Stoat', 'Stone',
        'Stork', 'Storm', 'Stream', 'Strike', 'Stump', 'Swallow', 'Swamp',
        'Swan', 'Sweet', 'Swift', 'Tall', 'Talon', 'Thistle', 'Thorn',
        'Thrift', 'Thyme', 'Tiger', 'Timber', 'Tip', 'Toad', 'Torn', 'Trout',
        'Tuft', 'Tulip', 'Tumble', 'Turtle', 'Twig', 'Vine', 'Violet', 'Vixen',
        'Vole', 'Warm', 'Wasp', 'Weasel', 'Web', 'Weed', 'Wet', 'Wheat', 'Whirl',
        'Whisker', 'Wild', 'Willow', 'Wind', 'Wisteria', 'Wolf', 'Wood',
        'Wren', 'Yarrow', 'Yew', 'Aardvark', 'Aardwolf', 'Agaric', 'Albatross',
        'Alfalfa', 'Algae', 'Almond', 'Aloe', 'Amanita', 'Amber', 'Antler', 'Aphid',
        'Apricot', 'Arc', 'Arching', 'Arctic', 'Arid', 'Arnica', 'Ashen', 'Asphodel', 'Aster',
        'Auburn', 'Avocet', 'Azalea', 'Bald', 'Barking', 'Barley', 'Basil', 'Bass', 'Beam', 'Beaming',
        'Bear', 'Bearberry', 'Beck', 'Belladonna', 'Bergamot', 'Betony', 'Beyond', 'Bison', 'Bistort',
        'Biting', 'Bitten', 'Bittern', 'Blaze', 'Bleak', 'Blink', 'Blinking', 'Blooming', 'Blossoming', 'Blotch',
        'Blotched', 'Blotchy', 'Bluebell', 'Boar', 'Bog', 'Bold', 'Bolete', 'Bolt', 'Bone', 'Bough', 'Bouncing',
        'Bounding', 'Brambling', 'Branching', 'Brazen', 'Bream', 'Breeze', 'Breezy', 'Brindled', 'Brine', 'Bristling',
        'Broom', 'Brush', 'Buck', 'Buffalo', 'Bugloss', 'Bumbling', 'Bunchberry', 'Bunting', 'Burn', 'Burned', 'Burnet',
        'Burning', 'Burnt', 'Burr', 'Burrow', 'Bush', 'Bushy', 'Butterbur', 'Buzz', 'Buzzing', 'Calling', 'Campion', 'Cardinal',
        'Carnation', 'Carp', 'Carrot', 'Catamount', 'Catkin', 'Cave', 'Chamomile', 'Chanterelle', 'Char', 'Charlock', 'Charred',
        'Chervil', 'Chick', 'Chickadee', 'Chicken', 'Chicory', 'Chipmunk', 'Chirp', 'Chrysalis', 'Chub', 'Cicada', 'Cindered',
        'Cindering', 'Cinquefoil', 'Clam', 'Clawed', 'Clawing', 'Clematis', 'Clouded', 'Cloudy', 'Coal', 'Comandra', 'Comfrey',
        'Coral', 'Cormorant', 'Cotton', 'Cougar', 'Coyote', 'Crab', 'Crag', 'Crane', 'Cream', 'Cress', 'Crocus', 'Crouched', 'Crouching',
        'Crying', 'Curlew', 'Curling', 'Currant', 'Dace', 'Daffodil', 'Dahlia', 'Damp', 'Dance', 'Dancing', 'Dandelion', 'Dapperling',
        'Dappled', 'Darkened', 'Darkening', 'Darling', 'Darner', 'Darter', 'Dash', 'Dawning', 'Deathcamas', 'Dewy', 'Dill', 'Dipper',
        'Ditch', 'Dock', 'Dog', 'Dot', 'Dotted', 'Downy', 'Dream', 'Dreamy', 'Dreaming', 'Drifted', 'Drifting', 'Driftwood', 'Drizzle',
        'Drop', 'Dropped', 'Dropping', 'Dry', 'Dune', 'Dunlin', 'Echoing', 'Eerie', 'Egg', 'Egret', 'Eider', 'Elder', 'Elk', 'Ermine', 'Evening',
        'Ewe', 'Fade', 'Faded', 'Fading', 'Falcon', 'Falling', 'Fang', 'Feathery', 'Fen', 'Field', 'Fiery', 'Fig', 'Fir', 'Fireweed', 'Fish', 'Fisher',
        'Fishy', 'Flailing', 'Flaming', 'Flare', 'Flashing', 'Flat', 'Flickering', 'Flight', 'Flighty', 'Flipped', 'Flipping', 'Flood', 'Flooded', 'Flooding',
        'Flowering', 'Flowery', 'Flurry', 'Fluttering', 'Fluttery', 'Flying', 'Fogging', 'Foggy', 'Forest', 'Freckled', 'Freeze', 'Freezing', 'Fritillary',
        'Frosted', 'Frosting', 'Frosty', 'Fumitory', 'Funnel', 'Galerina', 'Gannet', 'Garlic', 'Garter', 'Ginger', 'Ginkgo', 'Ginseng', 'Glade', 'Gleam',
        'Gleaming', 'Glimmer', 'Glimmering', 'Glory', 'Glow', 'Glowing', 'Gnarl', 'Gnarled', 'Goat', 'Gorge', 'Goshawk', 'Grackle', 'Grape', 'Grassy',
        'Gravely', 'Grayling', 'Grebe', 'Grisette', 'Grotto', 'Ground', 'Grounded', 'Grouse', 'Grove', 'Gulch', 'Gunnel', 'Gyrfalcon', 'Hailing', 'Halcyon',
        'Harrier', 'Hart', 'Harvest', 'Hatching', 'Hawker', 'Hawthorn', 'Heath', 'Hedge', 'Hedgenettle', 'Hemlock', 'Hen', 'Herring', 'Hilly', 'Hind',
        'Hooting', 'Hopping', 'Hornet', 'Howl', 'Howler', 'Howling', 'Humble', 'Hyacinth', 'Hyssop',
        'Icy', 'Ink', 'Inferno', 'Jackdaw', 'Jagged', 'Jumping', 'Kindle', 'Kinked', 'Knap', 'Koi', 'Labrador',
        'Land', 'Lantana', 'Larkspur', 'Leafy', 'Lemming', 'Lemon', 'Lightened', 'Lightening', 'Lilac', 'Lime',
        'Limpet', 'Lingonberry', 'Loch', 'Loon', 'Lotus', 'Lupine', 'Maggot', 'Magpie', 'Marshy', 'Marmot', 'Marten',
        'Mask', 'Masked', 'Mellow', 'Merlin', 'Mink', 'Minty', 'Misted', 'Misting', 'Mistletoe', 'Moor', 'Moose', 'Mottled',
        'Mountain', 'Muddle', 'Muddled', 'Muddy', 'Mumble', 'Mumbling', 'Murky', 'Nacre', 'Nightshade', 'Noisy', 'Nutty',
        'Oleander', 'Orange', 'Orchid', 'Oriole', 'Osprey', 'Oyster', 'Paling', 'Pasqueflower', 'Patched', 'Patchy', 'Path', 'Peach',
        'Peak', 'Peat', 'Peony', 'Pepper', 'Perching', 'Pheasant', 'Piper', 'Plover', 'Pond', 'Pool', 'Pooling', 'Poplar', 'Pouncing',
        'Prairie', 'Prickly', 'Primrose', 'Ptarmigan', 'Puffin', 'Raining', 'Rainy', 'Rapid', 'Raspberry', 'Reedy', 'Rippling', 'Rocky',
        'Rooster', 'Rooting', 'Rosy', 'Round', 'Runny', 'Rushing', 'Rusting', 'Rusty', 'Sap', 'Sapling', 'Salmon', 'Saxifrage', 'Scallop',
        'Scarred', 'Scarring', 'Scorched', 'Scorching', 'Seal', 'Seedling', 'Seedy', 'Senna', 'Shaded', 'Shadowed', 'Shadowy', 'Shady',
        'Shard', 'Sharpened', 'Shimmering', 'Shimmery', 'Shiny', 'Shining', 'Shrimp', 'Shrub', 'Silent', 'Silt', 'Silvery', 'Singing',
        'Skink', 'Skipper', 'Skipping', 'Skua', 'Skunk', 'Sleet', 'Slither', 'Slithering', 'Slope', 'Slug', 'Smoky', 'Snap',
        'Snapped', 'Snapping', 'Snapper', 'Snappy', 'Snarl', 'Snarling', 'Sneezing', 'Sneezy', 'Snipped', 'Snipping',
        'Snowed', 'Snowing', 'Snowy', 'Sooty', 'Sparking', 'Speckled', 'Splashed', 'Splashing', 'Spurge', 'Sporange',
        'Springing', 'Sprout', 'Spruce', 'Sprung', 'Squashberry', 'Stony', 'Storming', 'Stormy', 'Stream', 'Streaming',
        'Stricken', 'Striking', 'Striped', 'Strong', 'Stump', 'Stumpy', 'Summit', 'Sunning', 'Sunny', 'Swampy', 'Swiping',
        'Swirl', 'Swirling', 'Swooping', 'Tamarack', 'Tea', 'Tear', 'Tearing', 'Tern', 'Thorn', 'Thorny', 'Thundering',
        'Thunderous', 'Toad', 'Torrent', 'Traipse', 'Traipsed', 'Traipsing', 'Travel', 'Traveling', 'Tuft', 'Tufted', 'Tumbling',
        'Tunnel', 'Tussock', 'Twinflower', 'Umbra', 'Vervain', 'Veronica', 'Vulture', 'Walrus', 'Wander', 'Wandering',
        'Warren', 'Webbed', 'Webbing', 'Weedy', 'Wheat', 'Whelk', 'Whirling', 'Whisper', 'Whispering', 'Whistle', 'Wing',
        'Wish', 'Wishing', 'Wither', 'Withered', 'Withering', 'Wonder', 'Wondering', 'Wood', 'Wooded', 'Woody', 'Wort', 'Wound',
        'Wounded', 'Wounding', 'Wren', 'Yonder', 'Zinnia'
    ]

    colour_prefixes = {
        'WHITE': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Milk', 'Hail', 'Frost',
            'Ice', 'Sheep', 'Blizzard', 'Moon', 'Light', 'Bone', 'Icy', 'Frosted'
        ],
        'WHITE2': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Milk', 'Hail', 'Frost',
            'Ice', 'Sheep', 'Blizzard', 'Moon', 'Light', 'Bone', 'Icy', 'Frosted'
        ],
        'PALEGREY': [
            'Grey', 'Silver', 'Pale', 'Cloud', 'Hail', 'Frost', 'Ice', 'Mouse',
            'Bright', 'Fog', 'Foggy', 'Pebble', 'Light', 'Bone', 'Icy', 'Frosted'
        ],
        'SILVER': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue',
            'River', 'Blizzard', 'Bone', 'Icy', 'Frosted', 'Berry'
        ],
        'LILAC': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue',
            'River', 'Blizzard', 'Bone', 'Icy', 'Lilac', 'Lavender'
        ],
        'GREY': [
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', 'Fog', 'Bone', 'Pebble', 'Mountain', 'Cliff'
        ],
        'BLUE': [
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', 'Fog', 'Bone', 'Blue', 'Mist', 'Misty'
        ],
        'DARKGREY': [
            'Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Pebble', 'Cinder', 'Rock', 'Stone'
        ],
        'BLACK': [
            'Black', 'Black', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Scorched'
        ],
        'BLACK2': [
            'Black', 'Black', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Scorched'
        ],
        'DARK': [
            'Black', 'Black', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Brown', 'Shade', 'Dark', 'Night'
        ],
        'PALEGINGER': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Sandy', 'Creamy'
        ],
        'PALE': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Apricot', 'Sandy', 'Creamy'
        ],
        'CREAM': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Creamy', 'Sandy'
        ],
        'CREAM2': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Creamy', 'Sandy'
        ],
        'GOLDEN': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion'
        ],
        'GINGER': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', 'Plum'
        ],
        'APRICOT': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', 'Apricot'
        ],
        'ORANGE': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', 'Pumpkin'
        ],
        'DARKGINGER': [
            'Red', 'Pumpkin', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox'
        ],
        'LIGHTBROWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel', 'Muddy'
        ],
        'CARAMEL': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Cream',
            'Hazel', 'Fawn'
        ],
        'FAWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Deer',
            'Hazel', 'Fawn'
        ],
        'BROWN': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer'
        ],
        'CINNAMON': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Cinnamon',
            'Acorn', 'Mud', 'Deer'
        ],
        'CHOCOLATE': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Cocoa',
            'Acorn', 'Mud', 'Deer'
        ],
        'DARKBROWN':
        ['Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud',
         'Muddy', 'Moose', 'Shadow']
    }

    eye_prefixes = {
        'YELLOW': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light', 'Sun', 'Sunny', 'Bright', 'Marigold', 'Bee', 'Bumble', 'Sunflower', 'Dandelion', 'Wasp', 'Hive', 'Petal'],
        'AMBER': ['Amber', 'Sun', 'Fire', 'Gold', 'Honey', 'Scorch', 'Ember', 'Flame', 'Flaming', 'Orange', 'Butterfly', 'Monarch', 'Pumpkin', 'Carrot', 'Rust', 'Rusty'],
        'HAZEL': ['Tawny', 'Hazel', 'Gold', 'Daisy', 'Sand', 'Sandy', 'Hazelnut', 'Golden', 'Flower', 'Pale', 'Olive', 'Herb', 'Calm', 'Birch', 'Fawn', 'Spring'],
        'PALEGREEN': ['Green', 'Pale', 'Mint', 'Fern', 'Holly', 'Clover', 'Lime', 'Thyme', 'Pale', 'Light', 'Grass', 'Parsley', 'Leaf', 'Tansy', 'Herb', 'Thyme'],
        'GREEN': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsley', 'Grass', 'Leaf', 'Forest', 'Turtle', 'Lime'],
        'BLUE': ['Blue', 'Ice', 'Sky', 'Lake', 'Frost', 'Water', 'Ocean', 'Lake', 'Borage', 'Splash', 'Sapphire', 'Stream', 'Puddle', 'River', 'Sky', 'Mist', 'Misty'],
        'DARKBLUE': ['Blue', 'Sky', 'Lake', 'Berry', 'Dark', 'Water', 'Deep', 'Ocean', 'Lake', 'Borage', 'Splash', 'Sapphire', 'Stream', 'Blueberry', 'Berry', 'Sea'],
        'BLUEYELLOW': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light', 'Sun', 'Blue', 'Ice', 'Sky', 'Lake', 'Frost', 'Water', 'Ocean', 'Lake', 'Bee', 'Blueberry', 'Wasp'],
        'BLUEGREEN': ['Blue', 'Ice', 'Sky', 'Lake', 'Frost', 'Water', 'Ocean', 'Lake', 'Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Calm', 'Thyme', 'Blueberry', 'Sage'],
        'PALEYELLOW': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light', 'Sun', 'Dandelion', 'Marigold', 'Bee', 'Bumble', 'Sunflower', 'Dandelion', 'Wasp', 'Hive', 'Pale'],
        'RED': ['Red', 'Crimson', 'Fire', 'Blood', 'Scorch', 'Flame', 'Flaming', 'Rose', 'Ember', 'Burnt', 'Burning', 'Poppy', 'Petal', 'Hidden', 'Cardinal', 'Robin'],
        'AQUA': ['Ocean', 'Sea', 'Turtle', 'Blue', 'Splash', 'River', 'Water', 'Stream', 'Aqua', 'River', 'Stream', 'Puddle', 'Turquoise', 'Green', 'Lake', 'Pond'],
        'PALEVIOLET': ['Purple', 'Magic', 'Magical', 'Moon', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Petal', 'Flower', 'Blossom'],
        'SAGE': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsley', 'Grass', 'Leaf', 'Forest', 'Sage', 'Serene'],
        'PALEBLUE': ['Blue', 'Sky', 'Moon', 'Borage', 'Splash', 'Pale', 'Serene', 'Cloud', 'Sapphire', 'Stream', 'River', 'Jay', 'Feather', 'Splash', 'Pale', 'Light'],
        'PINK': ['Petal', 'Flower', 'Rose', 'Pale', 'Soft', 'Primrose', 'Bloom', 'Strawberry', 'Blossom', 'Hibiscus', 'Berry', 'Pink', 'Sweet', 'Serene', 'Flower'],
        'VIOLET': ['Night', 'Purple', 'Magic', 'Magical', 'Moon', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Petal', 'Flower', 'Plum'],
        'BROWN': ['Oak', 'Brown', 'Tree', 'Bark', 'Alder', 'Branch', 'Twig', 'Stem', 'Mud', 'Mouse', 'Dust', 'Acorn', 'Timber', 'Log', 'Brown', 'Dusky', 'Dusk', 'Dust'],
        'SPRINGGREEN': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsely', 'Bright', 'Spring', 'Light', 'Stem', 'Leaf'],
        'GOLDEN': ['Bright', 'Gold', 'Golden', 'Amber', 'Yellow', 'Orange', 'Sun', 'Sunny', 'Shine', 'Shining', 'Moon', 'Light', 'Bright', 'Honey', 'Spring', 'Shiny'],
        'HONEY': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light', 'Bright', 'Sun', 'Sunny', 'Shine', 'Shining', 'Gold', 'Golden', 'Spring', 'Shiny', 'Hive', 'Bee', 'Bumble'],
        'COPPER': ['Copper', 'Brown', 'Orange', 'Redwood', 'Bright', 'Scorch', 'Flame', 'Fire', 'Adder', 'Fox', 'Rust', 'Rusty', 'Oak', 'Brown', 'Ember', 'Shiny', 'Hare'],
        'MAGENTA': ['Petal', 'Flower', 'Bloom', 'Blossom', 'Hibiscus', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Magenta', 'Flower', 'Petal'],
        'MINT': ['Mint', 'Minty', 'Cold', 'Blue', 'Splash', 'River', 'Water', 'Stream', 'Breeze', 'River', 'Stream', 'Puddle', 'Serene', 'Mist', 'Misty', 'Pale', 'Sky'],
        'EMERALD': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsely', 'Bright', 'Spring', 'Emerald', 'Jewel', 'Jade'],
        'PUMPKIN': ['Amber', 'Sun', 'Fire', 'Gold', 'Honey', 'Scorch', 'Ember', 'Flame', 'Flaming', 'Orange', 'Butterfly', 'Monarch', 'Pumpkin', 'Carrot', 'Rust', 'Rusty'],
        'ROSEGOLD': ['Rose', 'Pink', 'Coral', 'Gold', 'Golden', 'Bright', 'Shining', 'Sun', 'Light', 'Petal', 'Blooming', 'Flower', 'Spring', 'Shiny', 'Strawberry', 'Berry'],
        'GREENGOLD': ['Gold', 'Golden', 'Sun', 'Sunny', 'Spring', 'Green', 'Bright', 'Dandelion', 'Marigold', 'Herb', 'Clover', 'Emerald', 'Jade', 'Honey', 'Leaf', 'Sapling'],
        'PINKBLUE': ['Petal', 'Flower', 'Rose', 'Pale', 'Soft', 'Strawberry', 'Blossom', 'Pink', 'Flower', 'Stream', 'Sky', 'Blue', 'Sweet', 'Serene', 'Splash', 'Sapphire'],
        'DANDELION': ['Dandelion', 'Yellow', 'Sun', 'Sunny', 'Hazel', 'Tawny', 'Green', 'Spring', 'Bright', 'Clover', 'Marigold', 'Shining', 'Emerald', 'Honey', 'Leaf', 'Light'],
        'INDIGO': ['Ocean', 'Violet', 'Blue', 'Deep', 'Whale', 'Water', 'Dark', 'River', 'Lake', 'Splash', 'Hidden', 'Jewel', 'Sapphire', 'Lapis', 'Moon', 'Night', 'Ebony', 'Raven'],
        'AMARANTH': ['Hibiscus', 'Amaranth', 'Red', 'Pink', 'Bright', 'Light', 'Blossom', 'Strawberry', 'Cherry', 'Apple', 'Rose', 'Crimson', 'Ember', 'Fox', 'Flame', 'Flaming'],
        'CORAL': ['Coral', 'Pink', 'Bright', 'Light', 'Pale', 'Soft', 'Sweet', 'Petal', 'Blossom', 'Strawberry', 'Blooming', 'Primrose', 'Berry', 'Cloud', 'Flower', 'Serene'],
        'DARKGREEN': ['Dark', 'Green', 'Forest', 'Leaf', 'Grass', 'Fern', 'Ivy', 'Vine', 'Thyme', 'Herb', 'Clover', 'Holly', 'Stem', 'Night', 'Sage', 'Branch', 'Twig', 'Stem'],
        'DARKAMBER': ['Amber', 'Copper', 'Fire', 'Bear', 'Hidden', 'Scorch', 'Ember', 'Flame', 'Flaming', 'Dark', 'Butterfly', 'Monarch', 'Pumpkin', 'Brown', 'Rust', 'Rusty'],
        'SCARLET': ['Red', 'Crimson', 'Fire', 'Amber', 'Scorch', 'Flame', 'Flaming', 'Rose', 'Ember', 'Burnt', 'Burning', 'Scarlet', 'Bright', 'Hidden', 'Cardinal', 'Light']
    }

    loner_names = [
        "Haku", "Pichi", "Poki", "Nagi", "Jubie", "Bonbon", "Beans", "Aurora",
        "Maleficent", "Luna", "Eclipse", "Sol", "Star", "George", "Nightmare",
        "Bagel", "Monster", "Gargoyle", "Missile Launcher", "Rolo", "Rocket",
        "Void", "Abyss", "Vox", "Princess", "Noodle", "Duchess", "Cheesecake",
        "Callie", "Randy", "Ace", "Queeny", "Freddy", "Stella", "Rooster",
        "Sophie", "Maverick", "Seamus", 'Meowyman', "Pickles", "Lacy", "Lucy",
        "Knox", "Lugnut", "Bailey", "Azula", "Lucky", "Sunny", "Sadie", "Sox",
        "Bandit", "Onyx", "Quinn", "Grace", "Fang", "Ike", "Flower",
        "Whiskers", "Gust", "Peony", 'Human', "Minnie", "Buddy", "Mollie",
        "Jaxon", "Dunnock", "Firefly", "Cheese", "Sandwich", "Spam",
        "Broccoli", "Prickle", "Insect", "Grasshopper", "Coral", "Windy",
        "Sofa", "McChicken", "Purry", "Katy", "Mop", "Fishtail", "Roman",
        "Wishbone", "Nova", "Quimby", "Quest", "Nessie", "Niles", "Neil",
        "Nutella", "Nakeena", "Nuka", "Hughie", "Harvey", "Herc", "French",
        "Finch", "Frannie", "Flutie", "Purdy", "Free", "Glory", "Snek", "Indi",
        "Igor", "Jupiter", "Nintendo", "Jesse", "James", "Jethro", "Shampoo",
        "Joker", "Jinx", "Chaos", "Havoc", "Trouble", "Kingston", "King",
        "Kip", "Kong", "Ken", "Kendra", "Kisha", "Kermit", "Kelloggs",
        "Kodiak", "Klondike", "Ketchup", "KD", "Lupo", "Luigi", "Lily", "Lora",
        "Lee", "Lex", "Lester", "Makwa", "Madi", "Minna", "Moxie", "Mucha",
        "Manda", "Monte", "Riya", "Monzi", "Nisha", "Nemo", "Nitro", "Oops",
        "O'Leary", "Ophelia", "Olga", "Oscar", "Owen", "Porsche", "Ping",
        "Pong", "Quinzee", "Quickie", "Quagmire", "Quake", "Quinoa", "Roomba",
        "Riot", "Peanut Wigglebutt", "Ramble", "Rudolph", "Rum", "Reese",
        "Scotch", "Sneakers", "Schmidt", "Espresso", "Cocoa Puff", "Sonic",
        "Teufel", "Toni", "Torque", "Tempest", "Turbo", "Tetris", "Triscuit",
        "Tumble", "Voltage", "Vinnie", "Vaxx", "Venture", "Vida", "Guinness",
        "Polly", "Piper", "Pepper", "Lakota", "Dakota", "Bently", "Chinook",
        "Tiny", "Ula", "Union", "Uriel", "Orion", "Oakley", "Roselie",
        "Belle", "Benny", "Bumblebee", "Bluebell", "Chip", "Chocolate",
        "Cracker", "Dave", "Dolly", "Egg", "Frito", "Frank", "Gibby", "Jack",
        "Jenny", "Juliet", "Joob", "John", "Jimmy", "Jude", "Kenny", "Tom",
        "Oreo", "Mocha", "Ninja", "Cinderblock", "Pip", "Pipsqueak", "Milque",
        "Toast", "Molly Murder Mittens", "Flabby", "Crunchy", "Sorbet",
        "Vanilla", "Mint", "Nikki", "Pocket", "Tabbytha", "Gravy",
        "Potato", "Chewy", "Pumpernickel", "Pecan", "Old Man Sam", "Icecube",
        "Queso Ruby", "Pearl", "Jasper", "Stan", "Rose", "Mojo", "Kate",
        "Carmen", "Mange", "Chase", "Socks", "Tabby", "Jay", "Charlie", "L",
        "Poopy", "Crunchwrap", "Meow-meow", "Bede", "Smores", "Evilface",
        "Nick", "Mitski", "Ash", "Ah", "Violet", "Alcina", "Worm", "Monika",
        "Rat", "Bongo", "Bunny", "Viktor", "Steve", "Jewels", "Blu", "Rue",
        "Stinky", "Garnet", "Anita", "Sloane", "Emi", "Vivienne", "Amber",
        "Moon", "Twilight", "River", "Glass", "Goose", "Hunter", "Amity",
        "Stripes", "Cowbell", "Rory", "Lobster", "Slug", "Starfish", "Salmon",
        "Judy", "Johnny", "Kerry", "Evelyn", "Holly", "Bolt", "Millie",
        "Jessica", "Laku", "Dragonfly", "X’ek", "Silva", "Dreamy", "Decay",
        "Twister", "Shay", "Louis", "Oleander", "Spots", "Cream", "Omelet",
        "Gizmo", "Feather", "Twix", "Silver", "Ghost", "Wisp", "Obi Wan",
        "Pikachu", "Mango", "Via", "Olivia", "Mr. Whiskers", "Fluffy",
        "Shimmer", "Mimi", "Melody", "Leon", "Punk", "Mew", "Fern",
        "Marceline", "Whisper", "Skrunkly", "Stolas", "Rio", "Steven", "Pear",
        "Sekhmet", "Melon", "Ember", "Loona", "Saki", "Tiny", "Sandy",
        "Miles", "Mini", "Judas", "Zim", "Vinyl", "Rarity", "Trixie", "Sunset",
        "Anubis", "Armin", "Amy", "Alice", "Alec", "Baphomet", "Bean",
        "Bastet", "Birb", "Burm", "Chrissy", "Cherry", "Chief", "Crow",
        "Carrie", "Calvin", "Cookie", "Catie", "Charm", "Crab", "Charles",
        "Caroline", "Conan", "Cloud", "Charlie", "Cowboy", 'Burger', "Dune",
        "Dan", "Delilah", "Emerald", "Emy", "Erica", " Eddie", "Eda", "Ferret",
        "Fawn", "Fiver", "Fallow", "Ferry", "Gamble", "Grain", "Gir", "Hop",
        "Hot Sauce", "Habanero", "Taco Bell", "Cheetoman", "Queso", "Ruby",
        "Molly", "Murder", "Mittens", "Tabatha", "Sam", "Samantha", "Peanut",
        "Wigglebutt", "Zoe", "Cheeto", "Taco", "Max", "Sparky", "Cosmo", "Fred", 
        "Leo", "Tucker", "Minette", "Milo", "Fork", "Penny", "Zelda", "Jake", 
        "Felix", "Oliver", "Kitty", "Chloe", "Angel", "Samantha", "Muschi", 
        "Chicco", "Caramel", "Charlotte", "Chanel", "Lola", "Ollie", "Boo", 
        "Frankie", "Hotdog", "Beverly", "Mera", "Tasha", "Gremlin", "Magi",
        "Angel", "Pipsqueak", "Snip-Snap", "Slinky", "Dragon"
    ]

    if os.path.exists('saves/prefixlist.txt'):
        with open('saves/prefixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if os.path.exists('saves/suffixlist.txt'):
        with open('saves/suffixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 eyes=None,
                 pelt=None):
        self.status = status
        if prefix is None:
            if colour is None and eyes is None:
                self.prefix = random.choice(self.normal_prefixes)
            elif eyes is None:
                a = random.randint(0, 5)
                if a != 1:
                    self.prefix = random.choice(self.normal_prefixes)
                else:
                    self.prefix = random.choice(self.colour_prefixes[colour])
            elif colour is None:
                a = random.randint(0, 5)
                if a != 1:
                    self.prefix = random.choice(self.normal_prefixes)
                else:
                    self.prefix = random.choice(self.eye_prefixes[eyes])
            else:
                a = random.randint(0, 7)
                if a == 1:
                    self.prefix = random.choice(self.colour_prefixes[colour])
                elif a == 2:
                    self.prefix = random.choice(self.eye_prefixes[eyes])
                else:
                    self.prefix = random.choice(self.normal_prefixes)
        else:
            self.prefix = prefix
        if suffix is None:
            loop = True
            while loop:
                if pelt is None or pelt == 'SingleColour':
                    self.suffix = random.choice(self.normal_suffixes)
                else:
                    a = random.randint(0, 7)
                    if a == 1:
                        self.suffix = random.choice(self.pelt_suffixes[pelt])
                    elif a == 1 and self.pelt.name in ["Tortie", "Calico"]:
                        self.suffix = random.choice(self.tortie_pelt_suffixes)
                    else:
                        self.suffix = random.choice(self.normal_suffixes)
                if self.suffix != self.prefix.lower():
                    loop = False
        else:
            self.suffix = suffix

    def __repr__(self):
        if self.status in ["deputy", "warrior", "medicine cat", "elder"]:
            return self.prefix + self.suffix
        else:
            return self.prefix + self.special_suffixes[self.status]


names = Name()
