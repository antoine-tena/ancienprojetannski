import { defineStore } from 'pinia'

export interface Block {
  id: string
  type: string
  order: number
  props: {
    title?: string
    content?: string
    backgroundColor?: string
    textColor?: string
    buttonText?: string
    buttonUrl?: string
    imageUrl?: string
    [key: string]: any
  }
}

export const useEditorStore = defineStore('editor', {
  state: () => ({
    isEditing: false,
    isAdmin: false,
    blocks: [] as Block[],
    selectedBlockId: null as string | null
  }),

  getters: {
    selectedBlock: (state) => {
      if (!state.selectedBlockId) return null
      return state.blocks.find(block => block.id === state.selectedBlockId)
    },

    sortedBlocks: (state) => {
      return [...state.blocks].sort((a, b) => a.order - b.order)
    }
  },

  actions: {
    toggleEditing() {
      if (this.isAdmin) {
        this.isEditing = !this.isEditing
        if (!this.isEditing) {
          this.selectedBlockId = null
        }
      }
    },

    setAdmin(isAdmin: boolean) {
      this.isAdmin = isAdmin
    },

    setBlocks(blocks: Block[]) {
      this.blocks = blocks
    },

    selectBlock(blockId: string | null) {
      this.selectedBlockId = blockId
    },

    updateBlockField(blockId: string, field: string, value: any) {
      const block = this.blocks.find(b => b.id === blockId)
      if (block) {
        // Support nested props
        if (field.includes('.')) {
          const [parent, child] = field.split('.')
          if (parent === 'props' && block.props) {
            block.props[child] = value
          }
        } else if (field === 'props') {
          block.props = { ...block.props, ...value }
        } else {
          // @ts-ignore
          block[field] = value
        }
      }
    },

    updateBlockProps(blockId: string, props: Record<string, any>) {
      const block = this.blocks.find(b => b.id === blockId)
      if (block) {
        block.props = { ...block.props, ...props }
      }
    },

    reorderBlocks(newOrder: Block[]) {
      // Update order based on array index
      newOrder.forEach((block, index) => {
        const existingBlock = this.blocks.find(b => b.id === block.id)
        if (existingBlock) {
          existingBlock.order = index
        }
      })
      this.blocks = [...newOrder]
    },

    addBlock(block: Omit<Block, 'order'>) {
      const maxOrder = this.blocks.reduce((max, b) => Math.max(max, b.order), -1)
      this.blocks.push({
        ...block,
        order: maxOrder + 1
      } as Block)
    },

    removeBlock(blockId: string) {
      const index = this.blocks.findIndex(b => b.id === blockId)
      if (index !== -1) {
        this.blocks.splice(index, 1)
        if (this.selectedBlockId === blockId) {
          this.selectedBlockId = null
        }
      }
    },

    duplicateBlock(blockId: string) {
      const block = this.blocks.find(b => b.id === blockId)
      if (block) {
        const newBlock: Block = {
          ...block,
          id: `${block.type}-${Date.now()}`,
          order: block.order + 1
        }
        this.blocks.push(newBlock)
      }
    }
  }
})
