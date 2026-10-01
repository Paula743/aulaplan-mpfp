export type Role = 'ADMIN' | 'COORDINATOR' | 'VIEWER'

export interface UserProfile {
  uid: string
  email: string
  display_name?: string
  role: Role
  active: boolean
}

export interface CatalogRecord {
  id: string
  [key: string]: unknown
}

export interface CatalogField {
  key: string
  label: string
  type?: 'text' | 'number' | 'email' | 'select' | 'checkbox'
  required?: boolean
  options?: Array<{ label: string; value: string }>
  defaultValue?: string | number | boolean
}

export interface ScheduleEntry {
  offering_id: string
  subject_id: string
  teacher_id: string
  group_id: string
  room_id: string
  time_block_id: string
  day: string
  start_time: string
  end_time: string
}

export interface ScheduleVersion {
  version: number
  score: number
  entries: ScheduleEntry[]
}