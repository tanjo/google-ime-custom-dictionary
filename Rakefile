# coding: utf-8

namespace :list do

  desc '更新処理'
  task:organize do
    remove_duplicate_entries("all.txt", "all.txt")
  end

  # テキスト形式ファイルの重複行を削除し更にソート
  #
  # @param [String] input_path
  #
  # @param [String] output_path
  #
  # @return void
  #
  def remove_duplicate_entries(input_path, output_path)
    lines = Array.new

    File.open("all.txt") { |file|
      while line = file.gets
        lines << line.chomp
      end
    }

    lines.uniq!.sort!

    File.open("all.txt", "w") { |file|
      lines.each do |l|
        file.puts(l)
      end
    }

    return lines
  end

end
